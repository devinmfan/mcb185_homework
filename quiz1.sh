#Co-Authors: Devin Fan, Sophia Chen
echo "Real Name: Devin Fan"
echo "Linux Username: $USER"
gunzip -c dictionary.gz | grep "a" | grep -E "[moucfta]{4,}" | grep -v "[^moucfta]" | wc
gunzip -c dictionary.gz | grep "b" | grep -E "[tailnrb]{4,}" | grep -v "[^tailnrb]" | wc
gunzip -c dictionary.gz | grep "c" | grep -E "[maonidc]{4,}" | grep -v "[^maonidc]" | wc
gunzip -c dictionary.gz | grep "z" | grep -E "[anorgiz]{4,}" | grep -v "[^anorgiz]" | wc

gunzip -c jaspar2024_core.transfac.gz
