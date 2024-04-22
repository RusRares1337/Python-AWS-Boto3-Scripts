output "server-ip" {
    value = aws_instance.myapp-server.public_ip
}

output "server-ip2" {
    value = aws_instance.myapp-server-two.public_ip
}

output "server-ip3" {
    value = aws_instance.myapp-server-three.public_ip
}

output "ami_id" {
  value = data.aws_ami.amazon-linux-image.id
}