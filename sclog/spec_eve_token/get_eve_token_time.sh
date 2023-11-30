grep -E "current time microseconds:" ./spec_infer > each_token_time

awk '{print $NF}' each_token_time > token_time
rm each_token_time