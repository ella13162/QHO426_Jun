from abc import ABC, abstractmethod

class Tech(ABC):
  
  @abstractmethod
  def activate(self):
    pass

  @abstractmethod
  def deactivate(self):
    pass

if __name__ == "__main__":
  t = Tech()
  t.activate()
  t.deactivate()
  