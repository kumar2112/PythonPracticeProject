def ratcliff_obershelp(seq1, seq2):
    # Base case: if either sequence is empty, there is no match
    if not seq1 or not seq2:
        return 0, []
    
    # Step 1: Find the longest contiguous matching subsequence (LCMS)
    # This will hold the indices of the matched subsequence
    best_match = (0, 0)  # (start index in seq1, start index in seq2)
    max_len = 0
    
    # Compare every possible substring in seq1 with every substring in seq2
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            match_len = 0
            # Find the longest matching substring starting at seq1[i] and seq2[j]
            while (i + match_len < len(seq1) and 
                   j + match_len < len(seq2) and 
                   seq1[i + match_len] == seq2[j + match_len]):
                match_len += 1
            
            # Update the best match if we found a longer subsequence
            if match_len > max_len:
                max_len = match_len
                best_match = (i, j)
    
    print(best_match)
    # Step 2: If no match is found, return 0 similarity
    if max_len == 0:
        return 0, []
    
    # Step 3: Recursively apply the same logic to the unmatched parts of the sequences
    # Before and after the matched subsequence
    i, j = best_match
    before_seq1 = seq1[:i]
    before_seq2 = seq2[:j]
    after_seq1 = seq1[i + max_len:]
    after_seq2 = seq2[j + max_len:]
    
    # Recursively compare the parts before and after the match
    before_score, before_subseq = ratcliff_obershelp(before_seq1, before_seq2)
    after_score, after_subseq = ratcliff_obershelp(after_seq1, after_seq2)
    
    # Combine the results
    match_subseq = seq1[i:i + max_len]
    total_score = before_score + max_len + after_score
    
    # Return the combined matched subsequences and the similarity score
    return total_score, before_subseq + [match_subseq] + after_subseq

# Example usage
seq1 = "Abdule "
seq2 = "Abduel"

# Running the Ratcliff/Obershelp algorithm
score, matching_subsequences = ratcliff_obershelp(seq1, seq2)

# Output the similarity score and the matching subsequences
print("Similarity Score:", score)
print("Matching Subsequences:", matching_subsequences)
