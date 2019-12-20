from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(visual_basic)
    print()

    lang_list = [ruby, python, visual_basic]

    print("The dynamically typed languages are:")
    for lang in lang_list:
        if lang.is_dynamic() is True:
            print(lang.name)


if __name__ == '__main__':
    main()
