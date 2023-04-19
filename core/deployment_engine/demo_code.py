import math  
  
def compute_roots(input_coefficients = [2, 5, 3]):
    
    Coeff1 = input_coefficients[0]
    Coeff2 = input_coefficients[1]
    Coeff3 = input_coefficients[2]
    
    # Checking if roots are real or complex based on value of discriminant i.e b2-4ac
  
    discriminant = Coeff2 * Coeff2 - 4 * Coeff1 * Coeff3  
    discriminant_root = math.sqrt(abs(discriminant))  
    
    # Computing roots using formula (-b +/- root(b2-4ac))/2a
    
    # If discriminant is positive then roots are real and different
    if discriminant > 0:  
        print("Roots are real")  
        print((-Coeff2 + discriminant_root) / (2 * Coeff1))  
        print((-Coeff2 - discriminant_root) / (2 * Coeff1))  
    # If discriminant is zero then roots are real but same
    elif discriminant == 0:  
        print("Root is real")  
        print(-Coeff2 / (2 * Coeff1))  
    # If discriminant is negative then roots are complex
    else:  
        print("Roots are Complex")  
        print(- Coeff2 / (2 * Coeff1), "+", round(discriminant_root / (2 * Coeff1), 1), "i")  
        print(- Coeff2 / (2 * Coeff1), "-", round(discriminant_root / (2 * Coeff1), 1), "i")  