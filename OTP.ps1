# Função para gerar a chave
function Generate-Key {
    param (
        [int]$length
    )
    $key = ""
    for ($i = 0; $i -lt $length; $i++) {
        $key += [char](Get-Random -Minimum 0 -Maximum 256)
    }
    return $key
}

# Função para criptografar a mensagem
function OTP-Encrypt {
    param (
        [string]$message,
        [string]$key
    )
    $encrypted = ""
    for ($i = 0; $i -lt $message.Length; $i++) {
        $encrypted += [char]([byte][char]$message[$i] -bxor [byte][char]$key[$i])
    }
    return $encrypted
}

# Função para descriptografar a mensagem
function OTP-Decrypt {
    param (
        [string]$encrypted,
        [string]$key
    )
    $decrypted = ""
    for ($i = 0; $i -lt $encrypted.Length; $i++) {
        $decrypted += [char]([byte][char]$encrypted[$i] -bxor [byte][char]$key[$i])
    }
    return $decrypted
}

# Exemplo de uso
$message = "HELLO"
$key = Generate-Key -length $message.Length
$encrypted_message = OTP-Encrypt -message $message -key $key
$decrypted_message = OTP-Decrypt -encrypted $encrypted_message -key $key

Write-Output "Message: $message"
Write-Output "Key: $key"
Write-Output "Encrypted: $encrypted_message"
Write-Output "Decrypted: $decrypted_message"
