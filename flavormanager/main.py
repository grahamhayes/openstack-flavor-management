import sys

from cliff.app import App
from cliff.commandmanager import CommandManager


class FlavorManager(App):

    def __init__(self):
        super(FlavorManager, self).__init__(
            description='',
            version='0.1',
            command_manager=CommandManager('flavormanager.cmds'),
            deferred_help=True,
        )


def main(argv=sys.argv[1:]):
    myapp = FlavorManager()
    return myapp.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
