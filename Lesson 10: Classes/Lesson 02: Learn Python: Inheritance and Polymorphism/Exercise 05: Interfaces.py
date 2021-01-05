# When two classes have the same method names and attributes, we say they implement the same interface.
# An interface in Python usually refers to the names of the methods and the arguments they take.
# Other programming languages have more rigid definitions of what an interface is,
# but it usually hinges on the fact that different objects from different classes
# can perform the same operation (even if it is implemented differently for each class).

class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item

# Create subclass
class VehicleInsurance(InsurancePolicy):
  # Create get_rate method
  def get_rate(self):
    # Return .001 * price_of_insured_item
    return .001 * self.price_of_insured_item

# Create subclass
class HomeInsurance(InsurancePolicy):
  # Create get_rate method
  def get_rate(self):
    # Return .00005 * price_of_insured_item
    return .00005 * self.price_of_insured_item
