{ pkgs ? import <nixpkgs> {} }:
let
  my-python = pkgs.python3;
  python-with-my-packages = my-python.withPackages (p: with p; [
    pygments
  ]);
in
pkgs.mkShell {
  name = "opencompl";
  
  packages = [
    python-with-my-packages
    pkgs.gnumake
    # other dependencies
  ];
}
