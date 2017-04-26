import numpy
from scipy.stats import norm


def unePosition(minLongeur, maxLongueur, minLargeur,maxLargeur,minAngle,maxAngle):
    """
    Donne une valeur à 95% dans l'intervalle donnée selon une loi normal, pour les trois paramètres, x, y ,theta
    
    :param minLongeur: Position en x minimal
    :param maxLongueur: Position eb x maximal
    :param minLargeur: position eb y maximal
    :param maxLargeur: position eb y maximal
    :param minAngle: angle minimal
    :param maxAngle: angle maximal
    :return: Trois valeurs tirées de l'intervalle de confiance à 95%
    """
    x = numpy.random.normal((maxLargeur-minLargeur)/2, (maxLargeur - minLargeur) / (2*2.56))
    y = numpy.random.normal((maxLongueur-minLongeur)/2, (maxLongueur - minLongeur) / (2*2.56))
    theta = numpy.random.normal((maxAngle-minAngle)/2, (maxAngle - minAngle) / (2*2.56))
    return int(x), int(y),int(theta)

