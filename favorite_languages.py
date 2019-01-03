from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['shawn'] = 'python'
favorite_languages['oscar'] = 'python'
favorite_languages['marcos'] = 'php'
favorite_languages['ian'] = 'C#'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorte language is " +
        language.title())