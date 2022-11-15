{ pkgs }: {
    deps = [
        pkgs.python38Packages.pip
        pkgs.python39Packages.pip
        pkgs.python39Full
        pkgs.cowsay
    ];
}