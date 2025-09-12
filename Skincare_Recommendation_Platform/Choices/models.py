from django.db import models

# Create your models here.

class SkinTypeChoices(models.TextChoices):

    OILY = "oily", "Oily"
    DRY = "dry", "Dry"
    COMBINATION = "combination", "Combination"
    SENSITIVE = "sensitive", "Sensitive"
    NORMAL = "normal", "Normal"

class ProductCategoryChoices(models.TextChoices):

    CLEANSER = "cleanser", "Cleanser"
    SERUM = "serum", "Serum"
    MOISTURIZER = "moisturizer", "Moisturizer"
    TONER = "toner", "Toner"
    SUNSCREEN = "sunscreen", "Sunscreen"

class PreferenceChoices(models.TextChoices):

    VEGAN = "vegan", "Vegan"
    FRAGRANCE_FREE = "fragrance-free", "Fragrance-Free"
    CRUELTY_FREE = "cruelty-free", "Cruelty-Free"
    ALCOHOL_FREE = "alcohol-free", "Alcohol-Free"
    NON_COMEDOGENIC = "non-comedogenic", "Non-Comedogenic"

class SkinConcernsChoices(models.TextChoices):

    ACNE_PRONE = "acne_prone", "Acne_Prone"
    REDNESS = "redness", "Redness"
    DARK_SPOTS = "dark_spots", "Dark Spots"
    AGING = "aging", "Early Signs of Aging"
    DULLNESS = "dullness", "Dullness"
    HYPERPIGMENTATION = "hyperpigmentation", "Hyperpigmentation"
    OILY_OR_BLACKHEADS = 'oily_or_blackheads', 'Oily/Blackheads'
    DRYNESS = 'dryness', 'Dryness & Dehydration'
    MATURE_SKIN = 'mature_skin', 'Mature Skin'
    SENSITIVE = 'sensitive', 'Sensitive / Rosacea-prone'

class DeviseChoices(models.TextChoices):

    MOBILE = 'mobile', "Mobile"
    DESKTOP = 'desktop', 'Desktop'

class IngredientsChoices(models.TextChoices):

    NIACINAMIDE = 'niacinamide','Niacinamide'
    HYALURONIC_ACID = 'hyaluronic_acid','Hyaluronic Acid'
    SALICYLIC_ACID = 'salicylic_acid','Salicylic Acid'
    RETINOL = 'retinol','Retinol'
    VITAMIN_C = 'vitamin_c','Vitamin C'
    CERAMIDES = 'ceramides','Ceramides'
    GLYCOLIC_ACID = 'glycolic_acid','Glycolic Acid'
    ZINC_OXIDE = 'zinc_oxide','Zinc Oxide'
    TEA_TREE_OIL = 'tea_tree_oil','Tea Tree Oil'
    ALOE_VERA = 'aloe_vera','Aloe Vera'

class InteractionTypeChoices(models.TextChoices):

    VIEW = 'view', 'View'
    LIKE = 'like', 'Like'
    CART = 'cart', 'Cart'

class SeasonChoices(models.TextChoices):
    
    SPRING = 'spring', 'Spring'
    SUMMER = 'summer', 'Summer'
    AUTUMN = 'autumn', 'Autumn'
    WINTER = 'winter', 'Winter'

class QuestionChoices(models.TextChoices):
    MULTIPLECHOICE = 'multiple_choice', 'Multiple Choice'
    SLIDER = 'slider', 'Slider'

class PlanChoices(models.TextChoices):
    FULL = 'full', 'Full Plan'
    HYDRATION = 'hydration', 'Hydration'
    MINIMALIST = 'minimalist', 'Minimalist'

class AgeGroupChoices(models.TextChoices):
    UNDER_20 = 'under_20', 'Under 20 years old'
    BETWEEN_20_30 = '20_30', '20 to 30 years'
    BETWEEN_30_40 = '30_40', '30 to 40 years'
    OVER_40 = 'over_40', 'Over 40 years old'

class LifeStyleChoices(models.TextChoices):
    MINIMAL = 'minimal', 'Short time (maximum 3 steps)'
    FULL = 'full', 'Desire for a complete routine (+5 steps)'
    HYDRATION = 'hydration', 'Focus on water supply'
    ANTI_AGING = 'anti_aging', 'Focus on anti-aging'

class BudgetChoices(models.TextChoices):
    LOW = 'low', 'Under 50$'
    MEDIUM = 'medium', '50$ to 100$'
    HIGH = 'high', '100$ to 250$'
    PREMIUM = 'premium', 'Over 250$'

class QuestionTypeChoices(models.TextChoices):
    TEXT = 'text', 'Text Answer'
    SINGLE_CHOICE = 'single_choice', 'Single Choice'
    MULTIPLE_CHOICE = 'multiple_choice', 'Multiple Choice'
    SLIDER = 'slider', 'Slider Scale'

class EyeConcernChoices(models.TextChoices):
    DARK_CIRCLES = 'dark_circles','Dark Circles'
    FINE_LINES_AND_WRINKLES = 'fine_lines_and_wrinkles','Fine Lines & Wrinkles'
    PUFFINESS = 'puffiness', 'Puffiness'
    NO_EYE_CONCERNS = 'no_eye_concern', 'No Eye Concern'