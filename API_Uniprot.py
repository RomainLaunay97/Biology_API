import requests

def uniprot_sequence_query(accessions,PFAM,taxonomy):
  f = open(f"sequences_{PFAM}_{taxonomy}.fasta", 'w')

  for i in range(0,len(accessions),100):
    subset_accessions=accessions[i:i+100]
    query = " OR ".join(f"accession:{acc}" for acc in subset_accessions)

    url = f"https://rest.uniprot.org/uniprotkb/stream?query={query}&format=fasta" # batch called more efficient than individual

    response = requests.get(url)
    response.raise_for_status()

    # Contenu FASTA
    fasta_data = response.text
    f.write(fasta_data)