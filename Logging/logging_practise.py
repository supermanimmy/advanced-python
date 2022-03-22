import logging 
import math

#Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename= r"log_files\Lumberjack.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode="w")

logger = logging.getLogger()



def quadratic_formula(a, b, c):
    """Return the solution to the equation ax^2 + bx + c = 0."""
    logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))

    # compute the discriminant
    logger.debug("# compute the discriminant")
    disc = b**2 - 4*a*c
    # compute the two roots
    logger.debug("# compute the two roots")
    root1= (-b + math.sqrt(disc))/ (2*a)
    root2= (-b - math.sqrt(disc))/ (2*a)

    #return the roots 
    logger.debug('#return the roots')
    return (root1, root2)
    
print(quadratic_formula(1, 0, -4))