import mysql.connector
from Bio import Entrez, SeqIO

# Set your email here; it's required by NCBI Entrez
Entrez.email = "sarthak.enigma@gmail.com"

# List of accession codes with their corresponding species type (as tuples)
accession_codes = [
  
    ("NM_007294", "Human (BRCA1)")
    
]

# Set the maximum length for the sequence to print
max_length = 1000  # Adjust this as needed

# Function to fetch sequences from NCBI and insert into the database
def fetch_and_insert_sequences(accession_list):
    # Connect to the MySQL database
    db = mysql.connector.connect(
        host="localhost",         # Change to your MySQL host
        user="root",      # Change to your database user
        password="mereces", # Change to your database password
        database="genome"  # Change to your database name
    )
    
    cursor = db.cursor()
    
    for accession, species in accession_list:
        try:
            # Fetch the sequence from NCBI
            handle = Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text")
            # Read the sequence data
            seq_record = SeqIO.read(handle, "fasta")
            handle.close()
            
            # Limit the sequence length to the first max_length characters
            sequence = str(seq_record.seq)[:max_length]
            
            # Map species to species_id
            species_name = species.split(" ")[0]  # Get the common name (first part)
            cursor.execute(f"SELECT species_id FROM Species WHERE common_name = '{species_name}'")
            species_id_result = cursor.fetchone()
            
            if species_id_result:
                species_id = species_id_result[0]
                
                # Insert into Genomic_data table
                insert_query = """
                INSERT INTO Genomic_data (species_id, source, sequence)
                VALUES (%s, %s, %s)
                """
                cursor.execute(insert_query, (species_id, accession, sequence))
                db.commit()
                print(f"Data for {species} inserted successfully.")
            else:
                print(f"No species_id found for {species}")
        
        except Exception as e:
            print(f"Could not retrieve or insert data for {species}: {e}")

    # Close the database connection
    cursor.close()
    db.close()

# Call the function to fetch and insert sequences
fetch_and_insert_sequences(accession_codes)
