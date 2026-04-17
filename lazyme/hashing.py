import hashlib


def md5(s, digest="int"):
    """From https://stackoverflow.com/a/13213664/610569"""
    if digest == "int":
        return int(hashlib.md5(s.encode("utf-8")).hexdigest(), 16)
    elif digest == "binary":
        return bin(int(hashlib.md5(s.encode("utf-8")).hexdigest(), 16))[2:]
    else:
        return hashlib.md5(s.encode("utf-8")).hexdigest()


def xxh64(s, seed=42, digest="int"):
    import xxhash

    h = xxhash.xxh64(s, seed=seed)
    if digest == "int":
        return h.intdigest()
    elif digest == "hex":
        return h.hexdigest()
    else:
        return h


def pivot_bitext(src, pivot1, pivot2, trg, outputfile="pivoted.tsv"):
    from tqdm import tqdm

    # Run the hash on the files.
    with open(pivot1) as fin:
        pivot1_hashes = [xxh64(line) for line in tqdm(fin)]
    with open(pivot2) as fin:
        pivot2_hashes = [xxh64(line) for line in tqdm(fin)]
    # Find the overlaps.
    overlaps = set(pivot1_hashes).intersection(pivot2_hashes)
    # Iterate through the first lang pair, populate `hash_to_src_pivot1`.
    with open(src) as sfin, open(pivot1) as tfin:
        hash_to_src_pivot1 = {
            hash: (s.strip(), t.strip())
            for s, t, hash in tqdm(zip(sfin, tfin, pivot1_hashes))
            if hash in overlaps
        }
    # Iterate through the second lang pair, print aligned output to file.
    with open(pivot2) as sfin, open(trg) as tfin, open(outputfile, "w") as fout:
        print("\t".join(["hash", "src", "pivot", "trg"]), end="\n", file=fout)
        for s, t, hash in tqdm(zip(sfin, tfin, pivot2_hashes)):
            s, t = s.strip(), t.strip()
            if hash in overlaps:
                src_txt, pivot1_txt = hash_to_src_pivot1[hash]
                if pivot1_txt == s:  # Check that there's no collison.
                    print("\t".join([str(hash), src_txt, s, t]), end="\n", file=fout)
