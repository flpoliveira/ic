<code>
TRUNCATE TABLE `flowStats`;
TRUNCATE TABLE `portStats`;
TRUNCATE TABLE `switch`;
</code>
<code>
SELECT `id`, `dpid`, `in-port`, `out-port`, `eth-src`, `eth-dst`, `ipv4-src`, `ipv4-dst`, `priority`, `packets`, `bytes`, `insertedTime` FROM `flowStats`;
</code>
From the linux shell prompt, use "sudo ovs-ofctl dump-flows s1". 
From the Mininet CLI prompt, use "dpctl show" or "sh ovs-ofctl dump-flows s1".
