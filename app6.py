from gooey import Gooey, GooeyParser

@Gooey(
    program_name="Data Processor",
    advanced=True,
    navigation="TABBED",
    show_sidebar=True,
    tabbed_groups=True
)
def main():
    parser = GooeyParser()
    group = parser.add_argument_group("Settings")
    group.add_argument("--input", required=True, widget="FileChooser")
    group.add_argument("--output", widget="DirChooser")
    
    advanced = parser.add_argument_group("Advanced")
    advanced.add_argument("--mode", choices=["Fast", "Slow"], default="Fast")
    advanced.add_argument("--debug", action="store_true")

    args = parser.parse_args()
    print(args)

if __name__ == "__main__":
    main()