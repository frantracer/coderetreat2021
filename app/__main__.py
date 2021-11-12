from .some_service import SomeService
from .thing import Thing


def main() -> None:
    service: SomeService = SomeService()
    print(service.service_call(5))

    thing: Thing = Thing(name="frantracer")
    print(thing.return_hello_name())


if __name__ == '__main__':
    main()
