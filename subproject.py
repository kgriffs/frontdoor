import frontdoor


REGISTRY = frontdoor.CommandRegistry('subproject')
cmd = REGISTRY.decorate


@cmd('build', 'Builds the subproject',
     'In a real project this might defer to another tool, such as Tox, or '
     'Maven, or CMake, etc etc. The important thing is the way to call the '
     'tool can be effectively documented here and standardized, which is '
     'helpful for polyglot projects (or for using new tools where the '
     'magical incantations may be hard to remember).')
def build(args):
    print("Builds something. Pretend this makes a subprocess call to "
          "make or something.")


@cmd('clean', 'Cleans the subproject',
     'Sort of like build, for for cleaning.')
def clean(args):
    print("Again, this would probably defer to another tool. But really it "
          "could be anything.")
