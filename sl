# Ativar firewall no switch
curl -X PUT http://localhost:8080/firewall/module/enable/0000000000000001
  [
    {
      "switch_id": "0000000000000001",
      "command_result": {
        "result": "success",
        "details": "firewall running."
      }
    }
  ]
curl -X PUT http://localhost:8080/firewall/module/enable/0000000000000002
  [
    {
      "switch_id": "0000000000000002",
      "command_result": {
        "result": "success",
        "details": "firewall running."
      }
    }
  ]


# Verificar se está ativo
curl http://localhost:8080/firewall/module/status

# Permitir comunicação todos protocolos h1 -> h2 
curl -X POST -d '{"nw_src": "10.0.0.1/32", "nw_dst": "10.0.0.2/32"}' http://localhost:8080/firewall/rules/0000000000000001
  [
    {
      "switch_id": "0000000000000001",
      "command_result": [
        {
          "result": "success",
          "details": "Rule added. : rule_id=2"
        }
      ]
    }
  ]
curl -X POST -d '{"nw_src": "10.0.0.2/32", "nw_dst": "10.0.0.1/32"}' http://localhost:8080/firewall/rules/0000000000000001
  [
    {
      "switch_id": "0000000000000001",
      "command_result": [
        {
          "result": "success",
          "details": "Rule added. : rule_id=1"
        }
      ]
    }
  ]

# Permitir comunicação todos protocolos h1 -> h3
## switch 1
curl -X POST -d '{"nw_src": "10.0.0.1/32", "nw_dst": "10.0.0.3/32"}' http://localhost:8080/firewall/rules/0000000000000001
  [
    {
      "switch_id": "0000000000000001",
      "command_result": [
        {
          "result": "success",
          "details": "Rule added. : rule_id=3"
        }
      ]
    }
  ]
curl -X POST -d '{"nw_src": "10.0.0.3/32", "nw_dst": "10.0.0.1/32"}' http://localhost:8080/firewall/rules/0000000000000001
  [
    {
      "switch_id": "0000000000000001",
      "command_result": [
        {
          "result": "success",
          "details": "Rule added. : rule_id=4"
        }
      ]
    }
  ]
## switch 2
curl -X POST -d '{"nw_src": "10.0.0.1/32", "nw_dst": "10.0.0.3/32"}' http://localhost:8080/firewall/rules/0000000000000002
  [
    {
      "switch_id": "0000000000000002",
      "command_result": [
        {
          "result": "success",
          "details": "Rule added. : rule_id=99"
        }
      ]
    }
  ]
curl -X POST -d '{"nw_src": "10.0.0.3/32", "nw_dst": "10.0.0.1/32"}' http://localhost:8080/firewall/rules/0000000000000002
  [
    {
      "switch_id": "0000000000000002",
      "command_result": [
        {
          "result": "success",
          "details": "Rule added. : rule_id=5"
        }
      ]
    }
  ]

#Permitir comunicação h2 -> h3
## switch 1
curl -X POST -d '{"nw_src": "10.0.0.2/32", "nw_dst": "10.0.0.3/32"}' http://localhost:8080/firewall/rules/0000000000000001
  [
    {
      "switch_id": "0000000000000001",
      "command_result": [
        {
          "result": "success",
          "details": "Rule added. : rule_id=9"
        }
      ]
    }
  ]
curl -X POST -d '{"nw_src": "10.0.0.3/32", "nw_dst": "10.0.0.2/32"}' http://localhost:8080/firewall/rules/0000000000000001
  [
    {
      "switch_id": "0000000000000001",
      "command_result": [
        {
          "result": "success",
          "details": "Rule added. : rule_id=10"
        }
      ]
    }
  ]
## switch 2
curl -X POST -d '{"nw_src": "10.0.0.2/32", "nw_dst": "10.0.0.3/32"}' http://localhost:8080/firewall/rules/0000000000000002
  [
    {
      "switch_id": "0000000000000002",
      "command_result": [
        {
          "result": "success",
          "details": "Rule added. : rule_id=97"
        }
      ]
    }
  ]
curl -X POST -d '{"nw_src": "10.0.0.3/32", "nw_dst": "10.0.0.2/32"}' http://localhost:8080/firewall/rules/0000000000000002
  [
    {
      "switch_id": "0000000000000002",
      "command_result": [
        {
          "result": "success",
          "details": "Rule added. : rule_id=8"
        }
      ]
    }
  ]

#Permitir comunicação h3 -> h4
curl -X POST -d '{"nw_src": "10.0.0.4/32", "nw_dst": "10.0.0.3/32"}' http://localhost:8080/firewall/rules/0000000000000002
  [
    {
      "switch_id": "0000000000000002",
      "command_result": [
        {
          "result": "success",
          "details": "Rule added. : rule_id=11"
        }
      ]
    }
  ]
curl -X POST -d '{"nw_src": "10.0.0.3/32", "nw_dst": "10.0.0.4/32"}' http://localhost:8080/firewall/rules/0000000000000002
  [
    {
      "switch_id": "0000000000000002",
      "command_result": [
        {
          "result": "success",
          "details": "Rule added. : rule_id=12"
        }
      ]
    }
  ]
# Permitir comunicação h4 -> h2
## switch 1
curl -X POST -d '{"nw_src": "10.0.0.2/32", "nw_dst": "10.0.0.4/32"}' http://localhost:8080/firewall/rules/0000000000000001
  [
    {
      "switch_id": "0000000000000001",
      "command_result": [
        {
          "result": "success",
          "details": "Rule added. : rule_id=13"
        }
      ]
    }
  ]
curl -X POST -d '{"nw_src": "10.0.0.4/32", "nw_dst": "10.0.0.2/32"}' http://localhost:8080/firewall/rules/0000000000000001
  [
    {
      "switch_id": "0000000000000001",
      "command_result": [
        {
          "result": "success",
          "details": "Rule added. : rule_id=14"
        }
      ]
    }
  ]
## switch 2
curl -X POST -d '{"nw_src": "10.0.0.2/32", "nw_dst": "10.0.0.4/32"}' http://localhost:8080/firewall/rules/0000000000000002
  [
    {
      "switch_id": "0000000000000002",
      "command_result": [
        {
          "result": "success",
          "details": "Rule added. : rule_id=15"
        }
      ]
    }
  ]
curl -X POST -d '{"nw_src": "10.0.0.4/32", "nw_dst": "10.0.0.2/32"}' http://localhost:8080/firewall/rules/0000000000000002
  [
    {
      "switch_id": "0000000000000002",
      "command_result": [
        {
          "result": "success",
          "details": "Rule added. : rule_id=16"
        }
      ]
    }
  ]


#Checar regras no switch
s1 ovs-ofctl -O openflow13 dump-flows s1