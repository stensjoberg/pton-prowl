#!/bin/python3

# Python imports
import urllib.request, io, string, traceback
from bs4 import BeautifulSoup

# Django imports
from django.core.management.base import BaseCommand, CommandError

# Project imports
from courses_groups.models import Course, CourseID

class Command(BaseCommand):
    help = "Imports courses from the Princeton Registrar Website"

    def handle(self, *args, **options):

        self.stdout.write("Accessing registrar's website...")

        # access url, get text and convert to BeautifulSoup object
        URL = 'https://registrar.princeton.edu/course-offerings/search_results.xml?submit=Search&term=1192&coursetitle=&instructor=&distr_area=&level=&cat_number=&sort=SYN_PS_PU_ROXEN_SOC_VW.SUBJECT%2C%20SYN_PS_PU_ROXEN_SOC_VW.CATALOG_NBR%2CSYN_PS_PU_ROXEN_SOC_VW.CLASS_SECTION%2CSYN_PS_PU_ROXEN_SOC_VW.CLASS_MTG_NBR'
        DEBUG_URL = 'https://registrar.princeton.edu/course-offerings/search_results.xml?term=1192&coursetitle=&instructor=&distr_area=&level=&cat_number=&subject=COS&sort=SYN_PS_PU_ROXEN_SOC_VW.SUBJECT%2C+SYN_PS_PU_ROXEN_SOC_VW.CATALOG_NBR%2CSYN_PS_PU_ROXEN_SOC_VW.CLASS_SECTION%2CSYN_PS_PU_ROXEN_SOC_VW.CLASS_MTG_NBR&submit=Search'
        u = urllib.request.urlopen(DEBUG_URL)
        f = io.TextIOWrapper(u, encoding='utf-8')
        text = f.read()
        soup = BeautifulSoup(text, "html.parser")

        self.stdout.write("Parsing and importing courses to database...")


        # tr is a section in registrars soup
        for course in soup.find_all('tr'):

            # unique course number one-to-one per course
            id = course.contents[1]

            # unique course id NOT one-on-one however
            course_codes = course.contents[3]

            # full natural langauge title of course
            title = course.contents[5]

            # try-except because some of the soup does not have string child
            try:
                id = int(unique_number.string)
                course_codes = courseids.stripped_strings
                title = title.string.replace('\n', '')

                course = Course(
                    id=id,
                    title=title,
                )

                self.stdout.write("Added course " + course.__str__())
                course.save()

                for code in course_codes:
                    code = id.replace(' ', '')
                    course_code = CourseCode(
                        code=code,
                        course=course
                    )
                    self.stdout.write("\tAdded ID " + code)
                    courseid.save()



            except Exception:
                self.stderr.write(traceback.format_exc())
