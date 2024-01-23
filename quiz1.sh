echo "Real Name: Devin Fan"
echo "Linux Username: $USER"
gunzip -c dictionary.gz | grep "r" | grep -E "[moucfta]{4,15}" | grep -v "[^moucfta]" | wc
gunzip -c dictionary.gz | grep "r" | grep -E "[tailnrb]{4,15}" | grep -v "[^tailnrb]" | wc
gunzip -c dictionary.gz | grep "r" | grep -E "[maonidc]{4,15}" | grep -v "[^maonidc]" | wc
gunzip -c dictionary.gz | grep "r" | grep -E "[anorgiz]{4,15}" | grep -v "[^anorgiz]" | wc
