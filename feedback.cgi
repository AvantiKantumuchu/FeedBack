#!/usr/bin/perl -wT
use strict; 
use CGI; 
use Fcntl qw(:flock);

my $cgi = new CGI;
my $email = $cgi->param( "email" );
my $age = $cgi->param( "age" ); 
my $feedback = $cgi->param( "feedback" );
my $sex = $cgi->param( "sex" ); 

my $salt = "21";

if($feedback eq "No opinion")
{
	my $enage = crypt($age,$salt);
	my $ensex = crypt($sex,$salt);
	print $cgi->header( "text/html" ),
	$cgi->start_html(
        -title    => "Encrypted Details for Major - CS",			
		-topmargin =>"0"
        ),
	
	$cgi->h1("Feedback Details : \n"),
	$cgi->h2("Email : $email\tAge : $age\tFeedback : $feedback\tSex : $sex\n"),
	$cgi->h2("Encrypted Major : $ensex\tEncrypted Age : $enage\n"),
	$cgi->end_html;    

}
else
{
		print $cgi->header( "text/html" ),
	$cgi->start_html(
        	-title    => "Welcome To XXX's Club",			
		-topmargin =>"0"
        ),
	
	$cgi->h1("Registration Details : \n"),
	$cgi->h2("Email : $email\tAge : $age\tFeedback : $feedback\tSex : $sex\n"),
	$cgi->end_html;    

}

