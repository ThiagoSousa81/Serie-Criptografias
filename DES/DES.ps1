# Função para gerar uma chave DES
function Generate-DESKey {
    $key = New-Object byte[] 8
    [System.Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($key)
    return $key
}

# Função para criptografar a mensagem usando DES
function DES-Encrypt {
    param (
        [string]$message,
        [byte[]]$key
    )
    
    $des = [System.Security.Cryptography.DESCryptoServiceProvider]::Create()
    $des.Key = $key
    $des.IV = $key # Usando a mesma chave como IV para simplicidade (não recomendado para produção)

    $encryptor = $des.CreateEncryptor()
    $messageBytes = [System.Text.Encoding]::UTF8.GetBytes($message)
    $encryptedBytes = $encryptor.TransformFinalBlock($messageBytes, 0, $messageBytes.Length)
    
    return [Convert]::ToBase64String($encryptedBytes)
}

# Função para descriptografar a mensagem usando DES
function DES-Decrypt {
    param (
        [string]$encryptedMessage,
        [byte[]]$key
    )
    
    $des = [System.Security.Cryptography.DESCryptoServiceProvider]::Create()
    $des.Key = $key
    $des.IV = $key # Usando a mesma chave como IV para simplicidade (não recomendado para produção)

    $decryptor = $des.CreateDecryptor()
    $encryptedBytes = [Convert]::FromBase64String($encryptedMessage)
    $decryptedBytes = $decryptor.TransformFinalBlock($encryptedBytes, 0, $encryptedBytes.Length)
    
    return [System.Text.Encoding]::UTF8.GetString($decryptedBytes)
}

# Exemplo de uso
$message = "HELLO"
$key = Generate-DESKey
$encrypted_message = DES-Encrypt -message $message -key $key
$decrypted_message = DES-Decrypt -encryptedMessage $encrypted_message -key $key

Write-Output "Message: $message"
Write-Output "Key: $([Text.Encoding]::UTF8.GetString($key))" # Exibe a chave em formato legível
Write-Output "Encrypted: $encrypted_message"
Write-Output "Decrypted: $decrypted_message"
