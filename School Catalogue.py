class School():
  def __init__(self, name, level, numberOfStudents):
    self.name = str(name)
    if level in ['primary', 'middle', 'high']:
      self.level = level
    else:
      raise ValueError('Invalid level')
    self.numberOfStudents =  int(numberOfStudents)
  
  def get_name(self):
    return self.name

  def get_level(self):
    return self.level

  def get_numberOfStudents(self):
    return self.numberOfStudents
  
  def set_numberOfStudents(self, newNumberOfStudents):
    self.numberOfStudents = newNumberOfStudents
  
  def __repr__(self):
    return f'A {self.level} school named "{self.name}" with {self.numberOfStudents} students.'

sl1 = School('BullyHouse', 'high', 348)
print(sl1.get_name())
print(sl1.get_level())
print(sl1.get_numberOfStudents())
print(sl1.__repr__())
sl1.set_numberOfStudents(386)
print(sl1)

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, 'primary', numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def get_pickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + f' The pickup policy is {self.pickupPolicy}'

psl1 = PrimarySchool('NerdDorm', 211, '3am')
print(psl1.get_name())
print(psl1.get_level())
print(psl1.get_numberOfStudents())
print(psl1.get_pickupPolicy())
print(psl1)

class MiddleSchool(School):
  def __init__(self, name, numberOfStudents):
    super().__init__(name, 'middle', numberOfStudents)
  
  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr

msl1 = MiddleSchool('ChillLounge', 461)
print(msl1.get_name())
print(msl1.get_level())
print(msl1.get_numberOfStudents())
print(msl1)

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'high', numberOfStudents)
    self.sportsTeams = sportsTeams
  
  def get_sportsTeams(self):
    return self.sportsTeams

  def __repr__(self):
    parentRepr = super().__repr__()
    sportsTeamsStr = ', '.join(self.sportsTeams)
    return parentRepr + f' With its sports Teams: {sportsTeamsStr}'

sportsTeams = ['Baseball', 'Tennis', 'Football', 'Basketball']
hsl1 = HighSchool('KaboomHigh', 531, sportsTeams)
print(hsl1.get_name())
print(hsl1.get_level())
print(hsl1.get_numberOfStudents())
print(hsl1.get_sportsTeams())
print(hsl1)
