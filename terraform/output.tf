output "website_endpoint" {
  description = "The public url of this website."
  value = "${aws_s3_bucket.b}"
}
