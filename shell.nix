{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShellNoCC {
  packages = [ pkgs.python3Minimal ];
}
