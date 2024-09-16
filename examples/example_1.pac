function FindProxyForURL(url, host) {
    if (shExpMatch(host, "*.localdomain.com") ||
        shExpMatch(host, "*.internal.company.com") ||
        isInNet(host, "192.168.0.0", "255.255.255.0")) {
        return "DIRECT HOST";
    }

    if (dnsDomainIs(host, ".example.com")) {
        return "PROXY proxy.example.com:8080";
    }

    if (url.indexOf("https://secure-site.com") === 0 ||
        url.indexOf("http://sensitive-data.com") === 0) {
        return "PROXY secureproxy.company.com:8080";
    }

    if (url.substring(0, 7) == "http://") {
        return "PROXY proxy.company.com:8080";
    }

    if (url.substring(0, 8) == "https://") {
        return "PROXY secureproxy.company.com:8080";
    }

    return "DIRECT";
}
