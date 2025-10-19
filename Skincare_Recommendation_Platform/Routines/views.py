from django.shortcuts import redirect, render
from django.http import HttpResponse
from Quizzes.models import QuizResults
from django.contrib.auth.decorators import login_required
from Products.models import Product
from Routines.models import RoutinePlan, RoutineStep

@login_required
def routine_generator_view(request):
    user = request.user
    try:
        quiz_data = QuizResults.objects.get(user=user)
    except QuizResults.DoesNotExist:
        return redirect('quiz_page')

    age = quiz_data.age

    preferences = quiz_data.preferences 

    skin_type = quiz_data.skin_type 

    concerns = quiz_data.concerns 
    
    budget = quiz_data.budget 
    
    eye_concern = quiz_data.eye_concern 
    
    dryness_level = quiz_data.dryness 

    routine_name = 'minimalist'
    if 'Dryness & Dehydration' in concerns or (skin_type == 'Dry' or dryness_level >= 7):
        routine_name = 'hydration'
    elif 'Dark Spots' in concerns or 'Hyperpigmentation' in concerns:
        routine_name = 'full'
    elif 'Acne-Prone' in concerns or skin_type == 'Oily':
        routine_name = 'minimalist'
    elif 'Early Signs of Aging' in concerns or 'Mature Skin' in concerns:
        routine_name = 'full'

    steps = []
    step = 1
    if skin_type == 'Oily':
        cleanser_name = Product.objects.filter(
            compatible_skin_types=['oily'],
            category='cleanser'
        ).first()
        if not cleanser_name:
            cleanser_name =  'Salicylic Acid Cleanser'
        
        steps.append({
            'order': step,
            'description': 'Use a foaming cleanser to control oil',
            'product_name': cleanser_name.name  # type: ignore
        })
        step+=1
    elif skin_type == 'Dry':
        if budget == 'Over 250$':
            steps.append({
                'order': step,
                'description': 'Use a cream cleanser for hydration',
                'product_name': 'Cream Cleanser'
            })
        else:
            cleanser_name = Product.objects.filter(
            compatible_skin_types=['dry'],
            category='cleanser',
            ).first()
            if not cleanser_name:
                cleanser_name = 'Simple Gentle'
            steps.append({
                'order': step,
                'description': 'Use a cream cleanser for hydration',
                'product_name': cleanser_name.name # type: ignore
            })
        step+=1
    else:
        if age == 'Over 40':
            steps.append({
                'order': step,
                'description': 'Use a gentle daily cleanser',
                'product_name': 'Gentle Cleanser'
            })
        elif age in ["Under 20","20 to 30"]:
            steps.append({
                'order': step,
                'description': 'Use a gentle daily cleanser',
                'product_name': 'Good Intent Glow Grind Cleansing Balm'
            })
        else:
            if budget == 'Over 250$' and preferences in ['Vegan', 'Cruelty-Free']:
                steps.append({
                'order': step,
                'description': 'Use a good cleanser',
                'product_name': 'Glacier Foam'
            })

            else:
                steps.append({
                    'order': step,
                    'description': 'Use a gentle daily cleanser',
                    'product_name': 'Salicylic Acid Cleanser'
                })
        step+=1

    concern_serums = {
        'Dark Spots': 'Glacier Foam',
        'Hyperpigmentation': 'Black Rice Bakuchiol Eye Cream',
        'Dryness & Dehydration': 'Hyaluronic Acid Serum',
        'Acne-Prone': 'Niacinamide Serum',
        'Early Signs of Aging': 'Resurfacing Retinol Serum',
        'Dullness': 'Hyaluronic Acid Serum',
        'Oily/Blackheads': 'Niacinamide Serum',
        'Redness': 'De-Bloat Soothing Eye Serum',
    }
    serum_added = False
    serums_added = []
    for concern in concerns:
        if concern in concern_serums:
            if(concern_serums[concern] not in serums_added):
                steps.append({
                    'order': step,
                    'description': f'Apply {concern_serums[concern]} to treat {concern.lower()}',
                    'product_name': concern_serums[concern]
                })
                serums_added.append(concern_serums[concern])
                serum_added = True
                step+=1

    if not serum_added:
        steps.append({
            'order': step,
            'description': 'Apply a basic hydrating serum',
            'product_name': 'Hyaluronic Acid Serum'
        })
    step+=1

    if budget in ["100$ to 250$","Over 250$"]:
        moisturizer_name = Product.objects.filter(
            compatible_skin_types=[skin_type],
            category='moisturizer',
        ).first()
        if not moisturizer_name:
            moisturizer_name = 'Oil-Free Moisturizer' if skin_type == 'Oily' else ('Anti-Aging Moisturizer' if 'Aging' in ' '.join(concerns) else 'Gentle Cleanser')
        steps.append({
            'order': step,
            'description': 'Use a moisturizer to seal hydration',
            'product_name': moisturizer_name
        })
        step+=1

    steps.append({
        'order': step,
        'description': 'Apply sunscreen with SPF 50 every morning',
        'product_name': 'SPF 50 Sunscreen'
    })
    step+=1

    if eye_concern != 'No Eye Concern':
        if budget in ["50$ to 100$","100$ to 250$"]:
            steps.append({
                'order': step,
                'description': f'Use an eye cream for {eye_concern.lower()}',
                'product_name': f'De-Bloat Soothing Eye Cream'
            })
        elif budget == "Over 250$":
            steps.append({
                'order': step,
                'description': f'Use an eye cream for {eye_concern.lower()}',
                'product_name': f'Black Rice Bakuchiol Eye Cream'
            })

    plan, _ = RoutinePlan.objects.get_or_create(user=user, name=routine_name)
    plan.routine_steps.all().delete() # type: ignore

    for step in steps:
        try:
            product = Product.objects.get(name__icontains=step['product_name'])
        except Product.DoesNotExist:
            product = None
        if product:
            RoutineStep.objects.create(
                routine_plan=plan,
                order=step['order'],
                description=step['description'],
                product=product
            )
        else:
            RoutineStep.objects.create(
                routine_plan=plan,
                order=step['order'],
                description=step['description'],
                product_name=step['product_name']
            )

    return render(request, 'Routines/routine_page.html', {'routine_plan': plan, 'routine_steps': list(plan.routine_steps.all())}) # type: ignore