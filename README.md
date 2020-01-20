CMS Demos
=========

Comparison Table
----------------

Aspect                          | Django CMS          | Mezzanine                | Wagtail
--------------------------------|---------------------|--------------------------|--------
Ownership Model                 |                     |                          | Open Source (Managed by Torchbox)
License                         |                     |                          |
Models                          |                     |                          |
Admin                           |                     |                          |
Installation | `pip install djangocms-installer` then `djangocms mysite -p path/to/mysite` | `pip install mezzanine` then `mezzanine-project mysite` | `pip install wagtail` then `wagtail start mysite`
Built-in Templates OOB          |                     | Yes (based on Bootstrap) | No
Add to existing Django project? | Yes (most involved) | Yes (in-between)         | Yes (simplest)
Known Incompatibilities         |                     |                          |
Custom User Model               |                     |                          | Yes (as long as it inherits from `AbstractBaseUser` and `PermissionsMixin`)


See also [Youtube: Comparing Wagtail, Django CMS and Mezzanine][yout01]


Potential Feature Considerations
--------------------------------

- Core functionality
- Security
- Managing assets
- Search
- Customization
- User interaction
- Roles and permissions
- Versioning
- SEO
- Support
- Integration with other systems

Aspect                          | Django CMS          | Mezzanine                | Wagtail
--------------------------------|---------------------|--------------------------|--------
Extensibility                   | Best                |                          | Good
Base Functionality              |                     |                          | Lightweight/Basic functionality
Django/Python Knowledge req'd   | Least               |                          | Most
Admin Interface                 | Less friendly       |                          | More friendly
API                             | ?                   | Yes                      | ?
Built-in Scheduling             | ?                   | No                       | ?
Maturity                        | Best                |                          | 


See also [Drupal, Django CMS, Wagtail and Mezzanine Comparison - Python vs PHP for CMS][netg01]


Wagtail Demo
------------

1. Create a project directory and venv
2. Install Django ([<2.3][wagt01]): `pip install 'django <2.3'`
3. Create a Django project: `django-admin startproject mysite .`
4. Create custom user model (must inherit from AbstractBaseUser and PermissionsMixin (which AbstractUser already does))
4. Install wagtail


[netg01]: https://www.netguru.com/blog/drupal-django-cms-wagtail-mezzanine-comparison-python-php
[yout01]: https://www.youtube.com/watch?v=3UC1MNFOjEI
[wagt01]: http://docs.wagtail.io/en/v2.7.1/getting_started/integrating_into_django.html
