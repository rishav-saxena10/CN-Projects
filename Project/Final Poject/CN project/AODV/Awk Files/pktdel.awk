BEGIN {
seqno = -1; 
droppedPackets = 0;
receivedPackets = 0;
count = 0;
}
{
#packet delivery ratio
if($4 == "RTR" && $1 == "s" && seqno < $6) {
seqno = $6;
} else if (( $1 == "r") && ( $7 == "cbr" || $7 =="tcp" ) && ( $4=="AGT" )) {receivedPackets++;
} else if ($1 == "D"){
droppedPackets++; 
}
#end-to-end delay
if($4 == "RTR" && $1 == "s") {
start_time[$6] = $2;
} else if(($7 == "cbr") && ($1 == "r")) {
end_time[$6] = $2;
} else if($1 == "D" && ( $7 == "cbr" || $7 =="tcp" )) {
end_time[$6] = -1;
}
}
END { 
print "\n";

print "Packet Delivery Ratio = " receivedPackets/(seqno+1)*100
"%";

print "\n";
}
