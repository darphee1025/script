#!/usr/bin/perl

use Cwd qw(getcwd abs_path);

my $cwd = getcwd();

print "current working Directory is $cwd\n";

my $full_path_cmd = abs_path($0);

print "$0's full path is : $full_path_cmd\n"
