import mysql.connector
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor, DistanceCalculator
from Bio.Align import MultipleSeqAlignment
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq  # Import Seq class

def fetch_sequence(species_id):
    # Connect to the database
    conn = mysql.connector.connect(
        user='root', 
        password='mereces', 
        host='localhost', 
        database='genome'
    )
    cursor = conn.cursor()
    
    # Query to fetch sequence based on species_id
    query = "SELECT Sequence FROM Genomic_Data WHERE Species_id = %s"
    cursor.execute(query, (species_id,))
    
    # Fetch the sequence
    sequence = cursor.fetchone()
    if sequence:
        return Seq(sequence[0])  # Convert to Seq object
    else:
        print(f"No sequence found for species_id {species_id}")
        return None

# Get species IDs from user input
species_id_1 = input("Enter the first species_id: ")
species_id_2 = input("Enter the second species_id: ")

# Fetch sequences for the given species IDs
seq1 = fetch_sequence(species_id_1)
seq2 = fetch_sequence(species_id_2)

# Check if both sequences were retrieved
if seq1 and seq2:
    records = [SeqRecord(seq1, id=species_id_1), SeqRecord(seq2, id=species_id_2)]
    alignment = MultipleSeqAlignment(records)
        
    calculator = DistanceCalculator('identity')
    dm = calculator.get_distance(alignment)
    constructor = DistanceTreeConstructor(calculator)
    tree = constructor.upgma(dm)
        
    # Calculate the evolutionary distance (for a simple case, get distance from distance matrix)
    evo_distance = dm[species_id_1, species_id_2]

        # Find the common ancestor
    common_ancestor = tree.common_ancestor({"name": species_id_1}, {"name": species_id_2})
    common_ancestor_name = common_ancestor.name if common_ancestor else "Unknown"

        # Store in the database
    # store_phylogenetic_data(species_id_1, species_id_2, evo_distance, common_ancestor_name)

        # Display the tree
    Phylo.draw_ascii(tree)
    print(f"Evolutionary distance: {evo_distance}")
    print(f"Common ancestor: {common_ancestor_name}")

else:
    print("Failed to retrieve both sequences for analysis.")
