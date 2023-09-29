
from app.db.models.team import Team
from app.schemas.team import TeamResponse


def prepare_team(team: Team) -> TeamResponse:
    return TeamResponse(
        id=team.id,
        name=team.name,
        location=team.location
    )
