#Co-Authors - Devin Fan, Sophia Chen
gunzip -c dictionary.gz | grep "r" | grep -E "[zoniacr]{4,15}" | grep -v "[^zoniacr]"