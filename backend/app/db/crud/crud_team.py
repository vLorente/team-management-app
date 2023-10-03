from app.db.crud.base import CRUDBase
from app.db.models.team import Team
from app.schemas.team import TeamCreate, TeamUpdate


class CRUDTeam(CRUDBase[Team, TeamCreate, TeamUpdate]):
    pass


team = CRUDTeam(Team)
