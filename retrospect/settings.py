"""
Django settings for retrospect project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
import operator
import os
import platform
import sys

p = platform.platform()
if operator.contains(p, 'Darwin'):  # 当我开发时的配置

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 源码方式安装第三方模块
    sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    # SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
    SECRET_KEY = 'fx!6ayzg#lk(6cptk1k)2^bhjg&k^q=k3p7l(*-i&p=%=%t6(e'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True
    # DEBUG = False
    TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'

    # ALLOWED_HOSTS = []
    ALLOWED_HOSTS = ['*', '192.168.1.104', '127.0.0.1']
    # Application definition

    SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
    SITE_ROOT = os.path.abspath(os.path.join(SITE_ROOT, '../'))

    INSTALLED_APPS = [
        'suit',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'django.contrib.sitemaps',
        'raven.contrib.django.raven_compat',
        'ckeditor',
        'ckeditor_uploader',
        'compressor',
        'pagedown',
        'haystack',
        # 'django_short_url',
        'import_export',
        'app',
    ]

    # Redirect url when short url not exists FIXME
    DJANGO_SHORT_URL_REDIRECT_URL = 'http://localhost:8000'

    MIDDLEWARE = [
        'django.middleware.cache.UpdateCacheMiddleware',  # 必须设置在第一个位置
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.gzip.GZipMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.http.ConditionalGetMiddleware',
        # 'blog.middleware.OnlineMiddleware',
        'django.middleware.cache.FetchFromCacheMiddleware',  # 必须设置在最后一个位置
    ]

    ROOT_URLCONF = 'retrospect.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages'
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'retrospect.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/1.10/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'retrospect',
            'USER': 'root',
            'PASSWORD': 'Ybkk1027',
            'HOST': '127.0.0.1',
            'PORT': 3306,
            'OPTIONS': {'charset': 'utf8mb4'},
        }
    }

    # Password validation
    # https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
    # https://docs.djangoproject.com/en/1.10/topics/i18n/

    IMPORT_EXPORT_USE_TRANSACTIONS = 'zh_Hans'

    LANGUAGE_CODE = 'zh-hans'

    TIME_ZONE = 'Asia/Shanghai'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.10/howto/static-files/
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'retrospect.whoosh_cn_backend.WhooshEngine',
            'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
        },
    }
    # 自动更新搜索索引
    HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
    # 允许使用用户名或密码登录
    # AUTHENTICATION_BACKENDS = ['accounts.user_login_backend.EmailOrUsernameModelBackend']

    STATIC_ROOT = os.path.join(SITE_ROOT, 'collectedstatic')
    STATIC_URL = '/static/'
    STATICFILES = os.path.join(BASE_DIR, 'static')

    # 图片和附件目录
    MEDIA_URL = '/media/'
    MEDIA_ROOT = (
        os.path.join(BASE_DIR, 'media')
    )

    TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
    DATE_TIME_FORMAT = '%Y-%m-%d'

    # bootstrap颜色样式
    BOOTSTRAP_COLOR_TYPES = [
        'default', 'primary', 'success', 'info', 'warning', 'danger'
    ]

    # 分页
    PAGINATE_BY = 10
    # http缓存时间
    CACHE_CONTROL_MAX_AGE = 2592000
    # cache setting
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
            'KEY_PREFIX': 'django_test' if TESTING else 'retrospect',
            'TIMEOUT': 60 * 60 * 10
        },
        'locmemcache': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'TIMEOUT': 10800,
            'LOCATION': 'unique-snowflake',
        }
    }

    SITE_ID = 1
    BAIDU_NOTIFY_URL = "http://data.zz.baidu.com/urls?site=https://www.lylinux.net&token=1uAOGrMsUm5syDGn"

    # Emial:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    # EMAIL_USE_TLS = True
    EMAIL_USE_SSL = True

    EMAIL_HOST = 'smtp.mxhichina.com'
    EMAIL_PORT = 465
    EMAIL_HOST_USER = os.environ.get('DJANGO_EMAIL_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('DJANGO_EMAIL_PASSWORD')
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
    SERVER_EMAIL = os.environ.get('DJANGO_EMAIL_USER')
    # 设置debug=false 未处理异常邮件通知
    ADMINS = [('liangliang', 'liangliangyy@gmail.com')]
    # 微信管理员密码(两次md5获得)
    WXADMIN = '995F03AC401D6CABABAEF756FC4D43C7'

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry', 'console', 'log_file'],
        },
        'formatters': {
            'verbose': {
                'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d %(module)s] %(message)s',
            }
        },
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse',
            },
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
        'handlers': {
            'log_file': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': 'retrospect.log',
                'maxBytes': 16777216,  # 16 MB
                'formatter': 'verbose'
            },
            'console': {
                'level': 'DEBUG',
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            },
            'null': {
                'class': 'logging.NullHandler',
            },
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'sentry': {
                'level': 'ERROR',  # To capture more than ERROR, change to WARNING, INFO, etc.
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
                'tags': {'custom-tag': 'x'},
            },
        },
        'loggers': {
            'retrospect': {
                'handlers': ['log_file', 'console', 'sentry'],
                'level': 'INFO',
                'propagate': True,
            },
            'django.request': {
                'handlers': ['mail_admins', 'sentry'],
                'level': 'ERROR',
                'propagate': False,
            },
            'raven': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
        }
    }

    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        # other
        'compressor.finders.CompressorFinder',
    )
    COMPRESS_ENABLED = False
    # COMPRESS_ENABLED = True
    # COMPRESS_OFFLINE = True

    COMPRESS_CSS_FILTERS = [
        # creates absolute urls from relative ones
        'compressor.filters.css_default.CssAbsoluteFilter',
        # css minimizer
        'compressor.filters.cssmin.CSSMinFilter'
    ]
    COMPRESS_JS_FILTERS = [
        'compressor.filters.jsmin.JSMinFilter'
    ]

    # ckeditor 编辑器
    CKEDITOR_IMAGE_BACKEND = "pillow"
    CKEDITOR_MEDIA_PREFIX = "static/ckeditor/"
    CKEDITOR_UPLOAD_PATH = "uploads/"
    CKEDITOR_CONFIGS = {
        'default': {
            'height': 400,
            'width': 800,
        },
        'full': {
            'toolbar': 'full',
            'height': 400,
            'width': 800,
        },
        'mini': {
            'toolbar': 'Basic',
            'height': 100,
            'width': 600,
        },
    }

    # # Markdown 编辑器
    # MDEDITOR_CONFIGS = {
    #     'default': {
    #         'width': '100% ',  # Custom edit box width
    #         'heigth': 500,  # Custom edit box height
    #         'toolbar': ["undo", "redo", "|",
    #                     "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase", "|",
    #                     "h1", "h2", "h3", "h5", "h6", "|",
    #                     "list-ul", "list-ol", "hr", "|",
    #                     "link", "reference-link", "image", "code", "preformatted-text", "code-block", "table", "datetime"
    #                                                                                                            "emoji",
    #                     "html-entities", "pagebreak", "goto-line", "|",
    #                     "help", "info",
    #                     "||", "preview", "watch", "fullscreen"],  # custom edit box toolbar
    #         'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],  # image upload format type
    #         'image_floder': 'editor',  # image save the folder name
    #         'theme': 'default',  # edit box theme, dark / default
    #         'preview_theme': 'default',  # Preview area theme, dark / default
    #         'editor_theme': 'default',  # edit area theme, pastel-on-dark / default
    #         'toolbar_autofixed': True,  # Whether the toolbar capitals
    #         'search_replace': True,  # Whether to open the search for replacement
    #         'emoji': True,  # whether to open the expression function
    #         'tex': False,  # whether to open the tex chart function
    #         'flow_chart': True,  # whether to open the flow chart function
    #         'sequence': True,  # Whether to open the sequence diagram function
    #         'mermaid': True,  # mermaid
    #         'vega': True,
    #     }
    # }

    # # suit 管理界面配置

    SUIT_CONFIG = {
        # header
        'ADMIN_NAME': u'珍柏追溯管理平台',
        'HEADER_DATE_FORMAT': 'Y年Fj日, l',
        'HEADER_TIME_FORMAT': 'H:i',

        # forms
        'SHOW_REQUIRED_ASTERISK': True,  # Default True
        'CONFIRM_UNSAVED_CHANGES': True,  # Default True

        # menu
        # 'SEARCH_URL': '/admin/auth/user/',
        # 'MENU_ICONS': {
        #    'sites': 'icon-leaf',
        #    'auth': 'icon-lock',
        # },
        'MENU_OPEN_FIRST_CHILD': True,  # Default True
        'MENU_EXCLUDE': ('Shorturl',),

        'MENU': (
            {'label': u'红酒追溯管理', 'models':
                (
                    {'label': u'产品管理', 'model': 'app.Wine'},
                    {'label': u'批次管理', 'model': 'app.Batch'},
                    {'label': u'核销管理', 'url': 'app.WineItem'},
                    {'label': u'活动管理', 'url': 'app.Activity'},
                    {'label': u'客户管理', 'url': 'app.WineUser'},
                )
             },
            {'label': u'网站设置', 'icon': 'icon-cog', 'models':
                (
                    {'label': u'域名设置', 'model': 'sites.site'},
                    {'label': u'轮播图设置', 'model': 'app.HomeAttach'},
                    {'label': u'组管理', 'model': 'auth.group'},
                    {'label': u'系统用户管理', 'model': 'auth.user'},
                )
             },
        ),

        # misc
        'LIST_PER_PAGE': 15
    }

    # 缓存配置
    CACHE_MIDDLEWARE_ALIAS = 'default'  # 用来存储的缓存别名
    CACHE_MIDDLEWARE_SECONDS = 1000  # 所有页面默认缓存时间,默认600
    CACHE_MIDDLEWARE_KEY_PREFIX = 'www.demo.com'  # 关键的前缀，当多个站点使用同一个配置的时候，这个可以设置可以避免发生冲突,一般设置为网站域名
    CACHE_MIDDLEWARE_ANONYMOUS_ONLY = False  # 那么只有匿名的请求会被缓存，这是一个禁用缓存非匿名用户页面的最简单的做法，注意确保已经启用了Django用户认证中间件
    CACHES = {
        'default': {
            # 'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',  # memcache 引擎
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',  # 调试引擎
            'LOCATION': [
                '127.0.0.1:11211',
            ],
            'TIMEOUT': None,  # 缓存超时时间（默认300，None表示永不过期，0表示立即过期）
            # 'OPTIONS': {
            # 'MAX_ENTRIES': 300,  # 最大缓存个数（默认300）
            # 'CULL_FREQUENCY': 3,  # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
            # },
            'KEY_PREFIX': '',  # 缓存key的前缀（默认空）
            'VERSION': 1,  # 缓存key的版本（默认1）
            # 'KEY_FUNCTION':函数名                                          # 生成key的函数（默认函数会生成为：【前缀:版本:key】）
            'MAX_ENTRIES': 2000
        }
    }


else:

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 源码方式安装第三方模块
    sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    # SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
    SECRET_KEY = 'fx!6ayzg#lk(6cptk1k)2^bhjg&k^q=k3p7l(*-i&p=%=%t6(e'

    # SECURITY WARNING: don't run with debug turned on in production!
    # DEBUG = True
    DEBUG = False
    TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'

    # ALLOWED_HOSTS = []
    ALLOWED_HOSTS = ['*', '192.168.1.104', '127.0.0.1']
    # Application definition

    SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
    SITE_ROOT = os.path.abspath(os.path.join(SITE_ROOT, '../'))

    INSTALLED_APPS = [
        'suit',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'django.contrib.sitemaps',
        'raven.contrib.django.raven_compat',
        'ckeditor',
        'ckeditor_uploader',
        'compressor',
        'pagedown',
        'haystack',
        # 'django_short_url',
        'import_export',
        'app',
    ]

    # Redirect url when short url not exists FIXME
    DJANGO_SHORT_URL_REDIRECT_URL = 'http://localhost:8000'

    MIDDLEWARE = [
        'django.middleware.cache.UpdateCacheMiddleware',  # 必须设置在第一个位置
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.gzip.GZipMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.http.ConditionalGetMiddleware',
        # 'blog.middleware.OnlineMiddleware',
        'django.middleware.cache.FetchFromCacheMiddleware',  # 必须设置在最后一个位置
    ]

    ROOT_URLCONF = 'retrospect.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages'
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'retrospect.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/1.10/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'retrospect',
            'USER': 'root',
            'PASSWORD': 'Hongjiu123',
            'HOST': '127.0.0.1',
            'PORT': 3306,
            'OPTIONS': {'charset': 'utf8'},
        }
    }

    # Password validation
    # https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
    # https://docs.djangoproject.com/en/1.10/topics/i18n/

    IMPORT_EXPORT_USE_TRANSACTIONS = 'zh_Hans'

    LANGUAGE_CODE = 'zh-hans'

    TIME_ZONE = 'Asia/Shanghai'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.10/howto/static-files/
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'retrospect.whoosh_cn_backend.WhooshEngine',
            'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
        },
    }
    # 自动更新搜索索引
    HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
    # 允许使用用户名或密码登录
    # AUTHENTICATION_BACKENDS = ['accounts.user_login_backend.EmailOrUsernameModelBackend']

    STATIC_ROOT = os.path.join(SITE_ROOT, 'collectedstatic')
    STATIC_URL = '/static/'
    STATICFILES = os.path.join(BASE_DIR, 'static')

    # 图片和附件目录
    MEDIA_URL = '/media/'
    MEDIA_ROOT = (
        os.path.join(BASE_DIR, 'media')
    )

    TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
    DATE_TIME_FORMAT = '%Y-%m-%d'

    # bootstrap颜色样式
    BOOTSTRAP_COLOR_TYPES = [
        'default', 'primary', 'success', 'info', 'warning', 'danger'
    ]

    # 分页
    PAGINATE_BY = 10
    # http缓存时间
    CACHE_CONTROL_MAX_AGE = 2592000
    # cache setting
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
            'KEY_PREFIX': 'django_test' if TESTING else 'retrospect',
            'TIMEOUT': 60 * 60 * 10
        },
        'locmemcache': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'TIMEOUT': 10800,
            'LOCATION': 'unique-snowflake',
        }
    }

    SITE_ID = 1
    BAIDU_NOTIFY_URL = "http://data.zz.baidu.com/urls?site=https://www.lylinux.net&token=1uAOGrMsUm5syDGn"

    # Emial:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    # EMAIL_USE_TLS = True
    EMAIL_USE_SSL = True

    EMAIL_HOST = 'smtp.mxhichina.com'
    EMAIL_PORT = 465
    EMAIL_HOST_USER = os.environ.get('DJANGO_EMAIL_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('DJANGO_EMAIL_PASSWORD')
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
    SERVER_EMAIL = os.environ.get('DJANGO_EMAIL_USER')
    # 设置debug=false 未处理异常邮件通知
    ADMINS = [('liangliang', 'liangliangyy@gmail.com')]
    # 微信管理员密码(两次md5获得)
    WXADMIN = '995F03AC401D6CABABAEF756FC4D43C7'

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry', 'console', 'log_file'],
        },
        'formatters': {
            'verbose': {
                'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d %(module)s] %(message)s',
            }
        },
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse',
            },
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
        'handlers': {
            'log_file': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': 'retrospect.log',
                'maxBytes': 16777216,  # 16 MB
                'formatter': 'verbose'
            },
            'console': {
                'level': 'DEBUG',
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            },
            'null': {
                'class': 'logging.NullHandler',
            },
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'sentry': {
                'level': 'ERROR',  # To capture more than ERROR, change to WARNING, INFO, etc.
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
                'tags': {'custom-tag': 'x'},
            },
        },
        'loggers': {
            'retrospect': {
                'handlers': ['log_file', 'console', 'sentry'],
                'level': 'INFO',
                'propagate': True,
            },
            'django.request': {
                'handlers': ['mail_admins', 'sentry'],
                'level': 'ERROR',
                'propagate': False,
            },
            'raven': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
        }
    }

    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        # other
        'compressor.finders.CompressorFinder',
    )

    # COMPRESS_ENABLED = False
    COMPRESS_ENABLED = True
    # COMPRESS_OFFLINE = True

    COMPRESS_CSS_FILTERS = [
        # creates absolute urls from relative ones
        'compressor.filters.css_default.CssAbsoluteFilter',
        # css minimizer
        'compressor.filters.cssmin.CSSMinFilter'
    ]
    COMPRESS_JS_FILTERS = [
        'compressor.filters.jsmin.JSMinFilter'
    ]

    # ckeditor 编辑器
    CKEDITOR_IMAGE_BACKEND = "pillow"
    CKEDITOR_MEDIA_PREFIX = "static/ckeditor/"
    CKEDITOR_UPLOAD_PATH = "uploads/"
    CKEDITOR_CONFIGS = {
        'default': {
            'height': 400,
            'width': 800,
        },
        'full': {
            'toolbar': 'full',
            'height': 400,
            'width': 800,
        },
        'mini': {
            'toolbar': 'Basic',
            'height': 100,
            'width': 600,
        },
    }

    # # Markdown 编辑器
    # MDEDITOR_CONFIGS = {
    #     'default': {
    #         'width': '100% ',  # Custom edit box width
    #         'heigth': 500,  # Custom edit box height
    #         'toolbar': ["undo", "redo", "|",
    #                     "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase", "|",
    #                     "h1", "h2", "h3", "h5", "h6", "|",
    #                     "list-ul", "list-ol", "hr", "|",
    #                     "link", "reference-link", "image", "code", "preformatted-text", "code-block", "table", "datetime"
    #                                                                                                            "emoji",
    #                     "html-entities", "pagebreak", "goto-line", "|",
    #                     "help", "info",
    #                     "||", "preview", "watch", "fullscreen"],  # custom edit box toolbar
    #         'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],  # image upload format type
    #         'image_floder': 'editor',  # image save the folder name
    #         'theme': 'default',  # edit box theme, dark / default
    #         'preview_theme': 'default',  # Preview area theme, dark / default
    #         'editor_theme': 'default',  # edit area theme, pastel-on-dark / default
    #         'toolbar_autofixed': True,  # Whether the toolbar capitals
    #         'search_replace': True,  # Whether to open the search for replacement
    #         'emoji': True,  # whether to open the expression function
    #         'tex': False,  # whether to open the tex chart function
    #         'flow_chart': True,  # whether to open the flow chart function
    #         'sequence': True,  # Whether to open the sequence diagram function
    #         'mermaid': True,  # mermaid
    #         'vega': True,
    #     }
    # }

    # # suit 管理界面配置

    SUIT_CONFIG = {
        # header
        'ADMIN_NAME': u'珍柏追溯管理平台',
        'HEADER_DATE_FORMAT': 'Y年Fj日, l',
        'HEADER_TIME_FORMAT': 'H:i',

        # forms
        'SHOW_REQUIRED_ASTERISK': True,  # Default True
        'CONFIRM_UNSAVED_CHANGES': True,  # Default True

        # menu
        # 'SEARCH_URL': '/admin/auth/user/',
        # 'MENU_ICONS': {
        #    'sites': 'icon-leaf',
        #    'auth': 'icon-lock',
        # },
        'MENU_OPEN_FIRST_CHILD': True,  # Default True
        'MENU_EXCLUDE': ('Shorturl',),

        'MENU': (
            {'label': u'红酒追溯管理', 'models':
                (
                    {'label': u'产品管理', 'model': 'app.Wine'},
                    {'label': u'批次管理', 'model': 'app.Batch'},
                    {'label': u'核销管理', 'url': 'app.WineItem'},
                    {'label': u'活动管理', 'url': 'app.Activity'},
                    {'label': u'客户管理', 'url': 'app.WineUser'},
                )
             },
            {'label': u'网站设置', 'icon': 'icon-cog', 'models':
                (
                    {'label': u'域名设置', 'model': 'sites.site'},
                    {'label': u'轮播图设置', 'model': 'app.HomeAttach'},
                    {'label': u'组管理', 'model': 'auth.group'},
                    {'label': u'系统用户管理', 'model': 'auth.user'},
                )
             },
        ),

        # misc
        'LIST_PER_PAGE': 15
    }

    # 缓存配置
    CACHE_MIDDLEWARE_ALIAS = 'default'  # 用来存储的缓存别名
    CACHE_MIDDLEWARE_SECONDS = 1000  # 所有页面默认缓存时间,默认600
    CACHE_MIDDLEWARE_KEY_PREFIX = 'www.demo.com'  # 关键的前缀，当多个站点使用同一个配置的时候，这个可以设置可以避免发生冲突,一般设置为网站域名
    CACHE_MIDDLEWARE_ANONYMOUS_ONLY = False  # 那么只有匿名的请求会被缓存，这是一个禁用缓存非匿名用户页面的最简单的做法，注意确保已经启用了Django用户认证中间件
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',  # memcache 引擎
            # 'BACKEND': 'django.core.cache.backends.dummy.DummyCache',  # 调试引擎
            'LOCATION': [
                '127.0.0.1:11211',
            ],
            'TIMEOUT': None,  # 缓存超时时间（默认300，None表示永不过期，0表示立即过期）
            # 'OPTIONS': {
            # 'MAX_ENTRIES': 300,  # 最大缓存个数（默认300）
            # 'CULL_FREQUENCY': 3,  # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
            # },
            'KEY_PREFIX': '',  # 缓存key的前缀（默认空）
            'VERSION': 1,  # 缓存key的版本（默认1）
            # 'KEY_FUNCTION':函数名                                          # 生成key的函数（默认函数会生成为：【前缀:版本:key】）
            'MAX_ENTRIES': 2000
        }
    }
