
from Bio import Entrez, SeqIO
from io import StringIO

Entrez.email = "your_email@example.com"

# Step 1: Read the IDs
ids = input.split

# Step 2: Store all downloaded FASTA records
records = []

for seq_id in ids:
    # Step 3: Download the record from NCBI
    with Entrez.efetch(
        db="nucleotide",
        id=seq_id,
        rettype="fasta",
        retmode="text"
    ) as handle:
        fasta_text = handle.read()

    # Step 4: Parse the FASTA record
    record = SeqIO.read(StringIO(fasta_text), "fasta")
    records.append(record)

# Step 5: Find the shortest record
shortest = min(records, key=lambda record: len(record.seq))

# Step 6: Print the complete FASTA record
print(f">{shortest.description}")
print(shortest.seq)
