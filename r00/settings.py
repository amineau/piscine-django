"""
Django settings for r00 project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Play settings
GRID = {
    'x': 20,
    'y': 20,
}
BEGIN = {
    'x': 9,
    'y': 0,
}
MOVIES = {
    0: 'Fight_Club',
    1: 'The_Exorcist',
    2: 'Pulp_Fiction',
    3: 'A_Clockwork_Orange',
    4: 'Reservoir_Dogs',
    5: 'Scarface',
    6: 'Snatch',
    7: 'Trainspotting',
    8: 'Shaun_of_the_Dead',
    9: 'French_Fried_Vacation',
    10: '300',
    11: 'Godzilla'
}

FULL_MOVIE = {
    'Fight_Club'                : {'box_office': 100.9, 'synopsis': 'The unnamed Narrator (Edward Norton) is a traveling automobile recall specialist who suffers from insomnia. When he is unsuccessful at receiving medical assistance for it, the admonishing doctor suggests he realize his relatively small amount of suffering by visiting a support group for testicular cancer victims. The group assumes that he, too, is affected like they are, and he spontaneously weeps into the nurturing arms of another man, finding a freedom from the catharsis that relieves his insomnia.', 'directed_by': 'the director', 'year': 2004, 'actors': ['Actor A', 'Actor B', 'Actor C'], 'poster': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Fight_Club.jpg/220px-Fight_Club.jpg'},
    'The_Exorcist'              : {'box_office': 12   , 'synopsis': 'Lankester Merrin is a veteran Catholic priest and exorcist who is on an archaeological dig in Iraq. There he finds an amulet that resembles the statue of Pazuzu, a demon whom Merrin had defeated years before. Merrin then realizes the demon has returned to seek revenge.', 'directed_by': 'the director', 'year': 2005, 'actors': ['Actor A', 'Actor B', 'Actor C'], 'poster': 'http://static.tvtropes.org/pmwiki/pub/images/theexorcist1973.jpg'},
    'Pulp_Fiction'              : {'box_office': 213.9, 'synopsis': 'Pulp Fictions narrative is told out of chronological order, and follows three main interrelated stories: mob contract killer Vincent Vega is the protagonist of the first story, prizefighter Butch Coolidge is the protagonist of the second, and Vincents partner Jules Winnfield is the protagonist of the third.[8] The stories intersect in various ways.', 'directed_by': 'the director', 'year': 2006, 'actors': ['Actor A', 'Actor B', 'Actor C'], 'poster': 'https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg'},
    'A_Clockwork_Orange'        : {'box_office': 26.6 , 'synopsis': 'In a futuristic London, Alex DeLarge is the leader of his "droogs", Georgie, Dim and Pete. One night, after getting intoxicated on drug-laden "milk-plus", they engage in an evening of "ultra-violence" including a fight with a rival gang led by Billyboy. They drive to the country home of writer F. Alexander and beat him to the point of crippling him for life. Alex then rapes his wife while singing "Singin in the Rain". The next day, while truant from school, Alex is approached by his probation officer Mr. P. R. Deltoid, who is aware of Alex s activities and cautions him.', 'directed_by': 'the director', 'year': 2007, 'actors': ['Actor A', 'Actor B', 'Actor C'], 'poster': 'https://upload.wikimedia.org/wikipedia/en/thumb/4/48/Clockwork_orangeA.jpg/220px-Clockwork_orangeA.jpg'},
    'Reservoir_Dogs'            : {'box_office': 2.8  , 'synopsis': 'Eight men eat breakfast at a Los Angeles diner before carrying out a diamond heist. Six of them use aliases: Mr. Blonde, Mr. Blue, Mr. Brown, Mr. Orange, Mr. Pink, and Mr. White. The others are mob boss Joe Cabot and his son and underboss "Nice Guy" Eddie Cabot, who are responsible for planning the job.', 'directed_by': 'the director', 'year': 2008, 'actors': ['Actor A', 'Actor B', 'Actor C'], 'poster': 'https://upload.wikimedia.org/wikipedia/en/thumb/f/f6/Reservoir_dogs_ver1.jpg/220px-Reservoir_dogs_ver1.jpg'},
    'Scarface'                  : {'box_office': 65.9 , 'synopsis': 'In 1980, Cuban refugee Antonio "Tony" Montana arrives in Miami, Florida, where he is sent to a refugee camp with his best friend Manny Ribera and their associates Angel and Chi-Chi. The four are released from the camp in exchange for assassinating a former Cuban government official at the request of wealthy drug dealer Frank Lopez, and they are given green cards. They become dishwashers in a diner.', 'directed_by': 'the director', 'year': 2009, 'actors': ['Actor A', 'Actor B', 'Actor C'], 'poster': 'https://upload.wikimedia.org/wikipedia/en/thumb/7/71/Scarface_-_1983_film.jpg/220px-Scarface_-_1983_film.jpg'},
    'Snatch'                    : {'box_office': 83.6 , 'synopsis': 'After stealing an 86-carat (17.2 g) diamond in a heist in Antwerp, Franky "Four-Fingers" goes to London to see diamond dealer Doug "The Head" on behalf of New York jeweler "Cousin Avi". One of the other robbers advises Franky to obtain a gun from ex-KGB agent Boris "The Blade". Meanwhile, Boris then plans to steal the diamond from him before he can turn it over to Doug.', 'directed_by': 'the director', 'year': 2010, 'actors': ['Actor A', 'Actor B', 'Actor C'], 'poster': 'https://upload.wikimedia.org/wikipedia/en/thumb/a/a7/Snatch_ver4.jpg/220px-Snatch_ver4.jpg'},
    'Trainspotting'             : {'box_office': 72   , 'synopsis': 'Heroin addict Mark Renton and his circle of friends are introduced: amoral con artist Simon "Sick Boy" Williamson (also an addict); slow-witted, kind-hearted Daniel "Spud" Murphy (another addict); clean-cut athlete Thomas "Tommy" MacKenzie; and the aggressive and pugnacious psychopath Francis "Franco" Begbie; picking fights with anybody who gets in his way.', 'directed_by': 'the director', 'year': 2011, 'actors': ['Actor A', 'Actor B', 'Actor C'], 'poster': 'https://upload.wikimedia.org/wikipedia/en/thumb/7/71/Trainspotting_ver2.jpg/250px-Trainspotting_ver2.jpg'},
    'Shaun_of_the_Dead'         : {'box_office': 30   , 'synopsis': 'Shaun is an electronics salesman with no direction in his life. His younger colleagues disrespect him, he is estranged from his stepfather Philip, and his girlfriend Liz is unhappy spending every date at his favourite pub, the Winchester.', 'directed_by': 'the director', 'year': 2012, 'actors': ['Actor A', 'Actor B', 'Actor C'], 'poster': 'https://upload.wikimedia.org/wikipedia/en/thumb/e/ec/Shaun-of-the-dead.jpg/220px-Shaun-of-the-dead.jpg'},
    'French_Fried_Vacation'     : {'box_office': 17.3 , 'synopsis': 'Gigi, Jerome, Christiane, Jean-Claude, and Bernard visit a resort in the Ivory Coast, the Club Med village of Assinie. Bernard subsequently meets up with his wife, Nathalie, who has already spent a week there, and they are all welcomed by Popeye and the eccentric emcees, Bobo and Bourseault.', 'directed_by': 'the director', 'year': 2013, 'actors': ['Actor A', 'Actor B', 'Actor C'], 'poster': 'https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Les_bronzes.jpg/220px-Les_bronzes.jpg'},
    '300'                       : {'box_office': 456  , 'synopsis': 'In 479 BC, one year after the famed Battle of Thermopylae, Dilios, a hoplite in the Spartan Army, begins his story by depicting the life of Leonidas I from childhood to kingship via Spartan doctrine.', 'directed_by': 'the director', 'year': 2014, 'actors': ['Actor A', 'Actor B', 'Actor C'], 'poster': 'https://upload.wikimedia.org/wikipedia/en/thumb/5/5c/300poster.jpg/220px-300poster.jpg'},
    'Godzilla'                  : {'box_office': 529.1, 'synopsis': 'n 1954, Godzilla, an ancient alpha predator, is lured to an island in an attempt to kill it with a nuclear bomb. In 1999, Monarch scientists Ishiro Serizawa (Ken Watanabe) and Vivienne Graham (Sally Hawkins) investigate a colossal skeleton unearthed in a collapsed mine in the Philippines. They find two giant spores; one dormant and one hatched with a trail that leads to the sea. In Japan, the Janjira Nuclear Power Plant experiences unusual seismic activity; Supervisor Joe Brody (Bryan Cranston) sends his wife Sandra (Juliette Binoche) with a team of other technicians into the reactor. A tremor breaches the reactor, leaving Sandra and her team unable to escape while the plant collapses.', 'directed_by': 'Gareth Edwards', 'year': 2015, 'actors': ['Aaron Taylor-Johnson', 'Actor B', 'Actor C'], 'poster': 'https://upload.wikimedia.org/wikipedia/en/1/10/Godzilla_%282014%29_poster.jpg'}
}

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '27o#g0!2!k%$8p)2a7&2q^2iyoygf-tq(v9oml5!&f24mnyc%e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'titleScreen',
    'worldMap',
    'battle',
    'movieDex',
    'options',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'r00.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'r00.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'templates', 'media'),
]
