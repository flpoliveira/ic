<code>
TRUNCATE TABLE `flowStats`;
TRUNCATE TABLE `portStats`;
TRUNCATE TABLE `switch`;
</code>

From the linux shell prompt, use "sudo ovs-ofctl dump-flows s1". 
From the Mininet CLI prompt, use "dpctl show" or "sh ovs-ofctl dump-flows s1".
