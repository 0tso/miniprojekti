from references import References
from console_io import ConsoleIO
from repositories.referencesrepository import ReferencesRepository
from services.reference_service import Services
from db_build import build

def init():
    build()
    console_io = ConsoleIO()
    ref_repo = ReferencesRepository()
    refe_services = Services(ref_repo)
    References(console_io, refe_services)

if __name__ == "__main__":
    init()
