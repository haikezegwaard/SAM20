from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpRequest
from niki.nikiconverter import NikiConverter
import logging
import json
# Create your views here.
# create a new summary, store it and render result

def nikisalecount(request):
    """
    Return sale status of project in cyfe data format
    """
    project = request.GET.get('project')
    nikimanager = NikiConverter()
    availability = nikimanager.getAvailability(project)
    result =  "Te koop, Optie, Verkocht\n"
    result += ",".join([str(i) for i in availability])+"\n"
    result += "Color,#00cb13,#ff7f00,#ee0000"
    return HttpResponse(result)


def nikirentcount(request):
    """
    Return rent status of project in cyfe data format
    """
    project = request.GET.get('project')
    nikimanager = NikiConverter()
    availability = nikimanager.getAvailability(project)
    result =  "Te huur, Optie, Verhuurd\n"
    result += ",".join([str(i) for i in availability])+"\n"
    result += "Color,#00cb13,#ff7f00,#ee0000"
    return HttpResponse(result)

def nikisaletable(request):
    """
    Return list of housetypes with according sale status
    """
    project = request.GET.get('project')
    nikimanager = NikiConverter()
    housetypes = nikimanager.getHouseTypes(project)
    result = ""
    for housetype in housetypes:
        sale = housetype.get('houses').get('for-sale') if housetype.get('houses').get('for-sale') else 0
        option = housetype.get('houses').get('option') if housetype.get('houses').get('option') else 0
        sold = housetype.get('houses').get('sold') if housetype.get('houses').get('sold') else 0
        result += '{},{},{},{}\n'.format(housetype.get('name'),sale,option,sold).replace(',', '&#44;')

    #result = "Woningtype,te koop, in optie, verkocht\n"
    return HttpResponse(result)

def nikirenttable(request):
    """
    Return list of housetypes with according rent status
    """
    project = request.GET.get('project')
    nikimanager = NikiConverter()
    housetypes = nikimanager.getHouseTypes(project)
    result = ""
    for housetype in housetypes:
        sale = housetype.get('houses').get('for-rent') if housetype.get('houses').get('for-rent') else 0
        option = housetype.get('houses').get('option') if housetype.get('houses').get('option') else 0
        sold = housetype.get('houses').get('rented') if housetype.get('houses').get('rented') else 0
        result += '{},{},{},{}\n'.format(housetype.get('name'),sale,option,sold).replace(',', '&#44;')

    #result = "Woningtype,te koop, in optie, verkocht\n"
    return HttpResponse(result)

def nikiglobalstats(request):
    """
    Return a list of miscellanious project properties
    """
    projectcode = request.GET.get('project')
    nikimanager = NikiConverter()
    project = nikimanager.apiRequest(projectcode)
    result = "Projecteigenschap,Beschikbaar,Totaal\n"
    result += "Projectvoortgang,-,{}\n".format(project.get('progress'))
    result += "Aantal woningen,"
    return HttpResponse(result)
    """


        $result = "Projecteigenschap,Beschikbaar,Totaal\n";
        $result.= "Projectvoortgang,-,".$niki->getProject($this->project)->{'progress'}."\n";
        $result.= "Aantal woningen,".$availablecount.",".$niki->getTotalHouseCount($this->project)."\n";
        $priceRangeTotal = $niki->getProjectPropertyRange($this->project, 'price-range');
        $priceRangeAvailable = $niki->getProjectPropertyRange($this->project, 'price-range', true);
        $result.= "Prijsklasse vanaf,".$priceRangeAvailable['min'].",".$priceRangeTotal['min']."\n";
        $result.= "Prijsklasse tot,".$priceRangeAvailable['max'].",".$priceRangeTotal['max']."\n";
        $livingSurfaceRangeTotal = $niki->getProjectPropertyRange($project,'livingsurface-range');
        $livingSurfaceRangeAvailable = $niki->getProjectPropertyRange($project,'livingsurface-range',true);
        $result.= "Oppervlakte vanaf,".$livingSurfaceRangeAvailable['min'].",".$allHouseStats['livingSurfaceMin']."\n";
        $result.= "Oppervlakte tot,".$livingSurfaceRangeAvailable['max'].",".$allHouseStats['livingSurfaceMax']."\n";
        return $result;"""

