from owlready2 import *
#https://pythonhosted.org/Owlready2/

path = "../ontology/"
file = "testOntologyGoT.owl"
GoT = get_ontology("file://" + path + file).load()

def main():
  print("\nListe des classes :\n",list(GoT.classes()))
  print("\nListe des instances :\n",list(GoT.individuals()))
  print("\nListe des propriétés :\n",list(GoT.object_properties()))

  print("\nListe des sous-classes de Place :\n",\
  GoT.search(subclass_of = GoT.Place))
  print("\nListe des entites avec le mot desire :\n",\
  GoT.search(iri = "*City"))
  print("\nListe des instances de Place :\n",\
  GoT.search(type = GoT.Place))
  print("\nListe des entites avec la relation desiree :\n",\
  GoT.search(isFromHouse = "*"))

  print("\nListe des parents de Jon Snow :\n",\
  GoT.Jon_Snow.isChildOf)

  print("\nTest propriete inverse, fils de Ned :\n",\
  GoT.Eddard_Stark.hasChild)

  print("\nTest propriete symétrique, frere et soeur :\n",\
  GoT.Daenerys_Targaryen.hasSibling,\
  GoT.Rhaegar_Targaryen.hasSibling)

  print("\nNouveau test, difference instance/attribut nom de l instance :")
  query = "Daenerys_Targaryen"
  test = GoT.Rhaegar_Targaryen.hasSibling[0]
  print("query\t\t:",query, "type :",type(query))
  print("individual\t:",test,"type :", type(test))
  print("query == test ?",query == test)
  test = GoT.Rhaegar_Targaryen.hasSibling[0].name
  print("query\t:",query, "type :",type(query))
  print("name\t:",test,"type :", type(test))
  print("query == test ?",query == test)

if __name__ == "__main__":
  main()
