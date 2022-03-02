from bego.models import History, Mission, OrgStructure
from regulations.models import Reglament, Penalty, Bonus
from for_bosses.models import Permissions
from departments.models import Department, Presentation
from soc_package.models import SocPackage


def sidebar_processor(request):
    bego_history = History.objects.prefetch_related('access').values('name', 'slug')
    bego_mission = Mission.objects.prefetch_related('access').values('name', 'slug')
    org_structure = OrgStructure.objects.prefetch_related('access').values('name', 'slug')
    reglaments = Reglament.objects.prefetch_related('access').values('name', 'slug')
    penalties = Penalty.objects.prefetch_related('access').values('name', 'slug')
    bonuses = Bonus.objects.prefetch_related('access').values('name', 'slug')
    departments = Department.objects.values('name', 'slug')
    presentations = Presentation.objects.all()
    soc_packages = SocPackage.objects.prefetch_related('access').values('name', 'slug')

    boss_permission = Permissions.objects.get(id=1)

    context = {
        'bego_history': bego_history,
        'bego_mission': bego_mission,
        'org_structure': org_structure,
        'reglaments': reglaments,
        'penalties': penalties,
        'bonuses': bonuses,
        'departments': departments,
        'presentations': presentations,
        'soc_packages': soc_packages,

        'boss_permission': boss_permission,
    }

    return context
