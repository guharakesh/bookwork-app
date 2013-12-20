import autocomplete_light
from models import Skill

autocomplete_light.register(Skill,
    search_fields=['^skill_text'],
    attrs={
        'placeholder': 'Skill ?',
        'data-widget-minimum-characters': 1,
    },
)
