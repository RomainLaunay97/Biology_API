from API_Interpro import output_uniprot_ids
import json


if __name__ == "__main__":
  search_files=["SearchResultsPotassiumChannel.json"]
  taxonomy_of_interest=["1", # All
                        "2", # Bacteria
                        "3379134", # Pseunomadoti
                        "1224", # Pseunomadota
                        "1236", # GammaProteoBacteria
                        "28216", # AlphaProteoBacteria
                        "28211", # BetaProteoBacteria
                        "356", # Hyphomicrobiales
                        ] # List of target taxons 

  # taxonomy_of_interest=[] # List of Subfamily
  # # output_list() # ecrire dans un fichier json
  # base_url = "https://www.ebi.ac.uk:443/interpro/api/protein/UniProt/entry/InterPro/IPR003967/taxonomy/uniprot/36298"
  # output_uniprot_ids(base_url) # ecrire dans un fichier json

### PARSE JSON
  for json_file in search_files:
    with open(json_file) as f:
      datas = json.load(f)
      
    for d in datas:
      # print(d["id"])
      # print(d["fields"]["source_database"][0])
      for taxon in taxonomy_of_interest:
        print(f"Search for familly {d["id"]} from {d["fields"]["source_database"][0]} and taxon {taxon}")
        output_uniprot_ids(f"https://www.ebi.ac.uk:443/interpro/api/protein/UniProt/entry/{d["fields"]["source_database"][0]}/{d["id"]}/taxonomy/uniprot/{taxon}",
                            d["id"],
                            taxon)