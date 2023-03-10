from django.shortcuts import render
from django.http import HttpResponse

def dmission(request):
    mission = """MISSION - The College of Computing and Multimedia Studies shall produce competent and innovative 
                professionals or Technopreneurs in the Information and Communication Technology (ICT) industry 
                adequately prepared in the practice of their profession supportive of national development goals
                and standards of global excellence."""

    return HttpResponse(mission)

def dvision(request):
    vission =  """VISSION - The College of Computing and Multimedia Studies shall be a center of excellence
                in delivering Computing and Multimedia education."""

    return HttpResponse(vission)

def dObjects(request):
    objects = """OBJECTS - After graduation, alumni of MSEUF-CCS program shall: 

                1.Be employed and demonstrate professionalism, competence and passion is solving contemporary 
                computing problems by developing or utilizing innovative IT solution;
                2. Embark in lifelong learning or research to attune to the continuous innovation in the IT 
                industry in order to adapt to the changing demands of the global market; and
                3. Exhibit leadership and teamwork, and commitment to their respective local or global 
                organizations."""

    return HttpResponse(objects); 



