def defang_ip_address(address):
    defanged_ip=""
    for ch in address:
        if ch==".":
            defanged_ip+="[.]"
        else:
            defanged_ip+=ch
    return defanged_ip


# Example usage:
ip_address = "192.168.1.1"
defanged_address = defang_ip_address(ip_address)
print(defanged_address)
