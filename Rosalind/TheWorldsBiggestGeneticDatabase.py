from Bio import Entrez

Entrez.email = "your_actual_email@example.com"

def count_genbank_entries(genus, start_date, end_date):
    query = (
        f'"{genus}"[Organism] AND '
        f'("{start_date}"[Publication Date] : '
        f'"{end_date}"[Publication Date])'
    )

    with Entrez.esearch(
        db="nucleotide",
        term=query,
        retmax=0
    ) as handle:
        record = Entrez.read(handle)

    return int(record["Count"])


# Example input
genus = "Anthoxanthum"
start_date = "2003/07/25"
end_date = "2005/12/27"

print(count_genbank_entries(genus, start_date, end_date))
'''
# Example input
genus = "Anthoxanthum"
start_date = "2003/07/25"
end_date = "2005/12/27"

print(count_genbank_entries(genus, start_date, end_date))
'''
