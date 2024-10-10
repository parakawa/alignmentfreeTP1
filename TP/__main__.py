from TP.loading import load_directory
from TP.kmers import enumerate_kmers, kmer2str



def jaccard(fileA, fileB, k):
    kmersA = set(enumerate_kmers(fileA, k))
    kmersB = set(enumerate_kmers(fileB, k))

    intersection = len(kmersA & kmersB)
    union = len(kmersA | kmersB)

    return intersection / union if union > 0 else 0



if __name__ == "__main__":
    print("Calcul de la similarité de Jaccard entre les fichiers")
    
    with open("resultats_jaccard.txt", "w") as f_out:

        files = load_directory("data")
        k = 21
        
        print("Calcul de la similarité de Jaccard")
        filenames = list(files.keys())
        for i in range(len(files)):
            for j in range(i + 1, len(files)):
                # on calcule la similarité de Jaccard pour chaque paire de fichiers
                similarity = jaccard(files[filenames[i]][0], files[filenames[j]][0], k)
                result = f"{filenames[i]} vs {filenames[j]} : Similarité de Jaccard = {similarity:.4f}"
                print(result)
                f_out.write(result + "\n") 

